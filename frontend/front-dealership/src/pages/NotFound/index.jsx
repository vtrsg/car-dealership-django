import React from 'react';
import { Link } from 'react-router-dom';
import { NotFoundArea } from './styled';

const NotFound = () => {
    return (
        <NotFoundArea>
            <h1>Page not found</h1>

            <Link to="/">Go to Home!!</Link>
        </NotFoundArea>
    );
};

export default NotFound;
