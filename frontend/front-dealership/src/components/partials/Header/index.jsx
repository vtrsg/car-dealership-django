import React from 'react';
import { HeaderArea } from './styled';
import { NavBar } from '../NavBar';

const Header = () => {
    return (
        <HeaderArea>
            <div className="container">
                <div className="logo">
                    <a href="/">
                        <span className="logoName">GARAGE</span>
                    </a>
                </div>
                <NavBar />
            </div>
        </HeaderArea>
    );
};

export default Header;
