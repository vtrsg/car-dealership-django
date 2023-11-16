import styled from 'styled-components';

export const NavBarArea = styled.div`
    nav {
        height: 45px;
        align-items: center;
        display: flex;

        ul,
        li {
            margin: 0;
            padding: 0;
            list-style: none;
        }
        ul {
            display: flex;
            gap: 10px;
        }
        li {
            text-align: center;
            a {
                border: 0;
                background: none;
                color: #333333;
                font-size: 1rem;
                text-decoration: none;
                cursor: pointer;

                &:hover {
                    color: #3374db;
                }
            }
            button {
                background-color: #3374db;
                border: 0;
                outline: 0;
                padding: 5px 10px;
                border-radius: 4px;
                color: #fff;
                font-size: 1rem;
                cursor: pointer;

                &:hover {
                    color: #3374db;
                    background-color: #ffffff;
                    border: 1px solid #3374db;
                }
            }
        }
    }

    .menuIcon {
        display: none;
        background: none;
        border: none;
        cursor: pointer;
    }

    .menuIcon span {
        display: block;
        width: 30px;
        height: 3px;
        margin: 6px 0;
        background-color: #333;
    }

    .overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
    }

    @media (max-width: 768px) {
        .navMenu nav,
        .navMenu ul {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 999;
        }

        .navMenu.open nav,
        .navMenu.open ul {
            display: flex;
        }

        .overlay {
            display: none;
        }

        .menuIcon {
            display: block;
        }

        .navMenu.open .overlay {
            display: block;
        }

        .navMenu nav ul {
            margin-top: 65px;
            flex-direction: column;
        }

        .navMenu nav li {
            width: 100%;
            text-align: center;

            a {
                margin-top: 15px;
                width: 100%;
                text-align: center;
                font-size: 1em;
                font-weight: bold;
                color: #3374db;
            }
        }
    }
`;
