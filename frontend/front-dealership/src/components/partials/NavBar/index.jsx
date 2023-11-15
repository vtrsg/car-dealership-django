import React, { useState } from 'react';
import { NavBarArea } from './styled';

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
                            <a href="/">Comprar carro</a>
                        </li>
                        <li>
                            <a href="/">Vender carro</a>
                        </li>
                        <li>
                            <button>Logout</button>
                        </li>
                        <li>
                            <a href="/">Comprar carro</a>
                        </li>
                        <li>
                            <a href="/">Vender carro</a>
                        </li>
                        <li>
                            <a href="/">Cadastrar</a>
                        </li>
                        <li>
                            <a href="/">Login</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </NavBarArea>
    );
};
