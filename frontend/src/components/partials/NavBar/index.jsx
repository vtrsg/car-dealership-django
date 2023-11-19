import React, { useState } from 'react';
import { NavBarArea } from './styled';
import { Link } from 'react-router-dom';
import { NavLink } from 'react-router-dom';

export const NavBar = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <NavBarArea>
            <div className={`navMenu ${menuOpen ? 'open' : ''}`}>
                <button className="menuIcon" onClick={toggleMenu}>
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <nav className={menuOpen ? 'overlay' : ''}>
                    <ul>
                        <li>
                            <Link href="/">Comprar carro</Link>
                        </li>
                        <li>
                            <Link href="/">Vender carro</Link>
                        </li>
                        <li>
                            <Link to="/create" component={NavLink}>
                                Cadastrar
                            </Link>
                        </li>
                        <li>
                            <Link to="/signin" component={NavLink}>
                                Login
                            </Link>
                        </li>
                        <li>
                            <button>Logout</button>
                        </li>
                    </ul>
                </nav>
            </div>
        </NavBarArea>
    );
};
