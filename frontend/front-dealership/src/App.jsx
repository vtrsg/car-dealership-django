import React from 'react';

import Template from './components/Template';
import Header from './components/partials/Header';
import Footer from './components/partials/Footer';
import './App.css';

const Page = (props) => {
    return (
        <Template>
            <Header />

            <Footer />
        </Template>
    );
};

export default Page;
