import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../context/AuthContext';
import Modal from './Modal';

const AppointmentHistory = () => {
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedAppointment, setSelectedAppointment] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const { user } = useContext(AuthContext);

  useEffect(() => {
    const fetchAppointments = async () => {
      if (!user) return;

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/user/appointments/', {
          params: { user_id: user.id } // Assuming you can pass user ID as a query parameter
        });
        setAppointments(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchAppointments();
  }, [user]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading appointments: {error.message}</p>;

  const handleViewDetails = (appointment) => {
    setSelectedAppointment(appointment);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedAppointment(null);
  };

  // Format the appointment date
  const formatDate = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  return (
    <div className='mt-16 p-4'>
      <h1 className='text-2xl font-bold mb-4'>My Appointments</h1>
      <ul className='space-y-4'>
        {appointments.map(appointment => (
          <li key={appointment.id} className='p-4 bg-white rounded-lg shadow-md'>
            <div className='flex items-center'>
              <p className='text-lg font-semibold mr-4'>{appointment.customer_name}</p>
              <p className='text-sm text-gray-600'>{formatDate(appointment.appointment_date)}</p>
            </div>
            <p className='text-sm text-gray-600'>{appointment.appointment_time}</p>
            <button
              onClick={() => handleViewDetails(appointment)}
              className='px-4 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700 transition-colors mt-2'
            >
              View Details
            </button>
          </li>
        ))}
      </ul>
      {selectedAppointment && (
        <Modal isOpen={isModalOpen} onClose={handleCloseModal}>
          <h3 className='text-lg font-semibold mb-2'>Appointment Details</h3>
          <p><strong>Customer:</strong> {selectedAppointment.customer_name}</p>
          <p><strong>Date:</strong> {formatDate(selectedAppointment.appointment_date)}</p>
          <p><strong>Time:</strong> {selectedAppointment.appointment_time}</p>
          <p><strong>Status:</strong> {selectedAppointment.status}</p>
          <p><strong>Checklist:</strong></p>
          <ul className='list-disc pl-5'>
            {selectedAppointment.checklist.map((item, index) => (
              <li key={index}>{item.text.name} - {item.done ? 'Completed' : 'Pending'}</li>
            ))}
          </ul>
        </Modal>
      )}
    </div>
  );
};

export default AppointmentHistory;
