import React from 'react';
import { HeaderArea } from './styled';
import { NavBar } from '../NavBar';
import { Link, NavLink } from 'react-router-dom';

const Header = () => {
    return (
        <HeaderArea>
            <div className="container">
                <div className="logo">
                    <Link to="/" component={NavLink}>
                        <span className="logoName">GARAGE</span>
                    </Link>
                </div>
                <NavBar />
            </div>
        </HeaderArea>
    );
};

export default Header;
