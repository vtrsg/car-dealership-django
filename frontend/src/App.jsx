import React from 'react';
import { BrowserRouter } from 'react-router-dom';

import Template from './components/Template';
import Header from './components/partials/Header';
import Footer from './components/partials/Footer';
import './App.css';
import Routes from './Routes.js';

const Page = (props) => {
    return (
        <BrowserRouter>
            <Template>
                <Header />

                <Routes />

                <Footer />
            </Template>
        </BrowserRouter>
    );
};

export default Page;
