import styled from 'styled-components';

export const HeaderArea = styled.div`
    background-color: #ffffff;
    height: 80px;
    border-bottom: 1px solid #ccc;
    display: flex;
    .container {
        width: 100%;
        margin: auto;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

    a {
        text-decoration: none;
    }

    .logo {
        .logoName {
            font-size: 30px;
            font-weight: bold;
            color: #3374db;
        }
    }
`;
