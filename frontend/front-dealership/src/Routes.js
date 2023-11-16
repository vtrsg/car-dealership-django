import React from 'react';
import { Routes, Route } from 'react-router-dom';

import SignIn from './pages/SignIn';
import Register from './pages/Register';
import NotFound from './pages/NotFound';

const routes = () => {
    return (
        <Routes>
            <Route exact path="/signin" element={<SignIn />} />
            <Route exact path="/create" element={<Register />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    );
};

export default routes;
