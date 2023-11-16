import React, { useEffect } from 'react';
import axiosInstance from '../../../services/api';
import { useNavigate } from 'react-router-dom';
import { SignUpArea } from './styled';

export const SignUp = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const response = axiosInstance.post('user/logout/blacklist/', {
            refresh_token: localStorage.getItem('refresh_token'),
        });
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        navigate('/login');
    });
    return <SignUpArea>Logout</SignUpArea>;
};
