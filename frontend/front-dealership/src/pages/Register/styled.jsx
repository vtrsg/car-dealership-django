import styled from 'styled-components';

export const PageArea = styled.div`
    form {
        background-color: #fff;
        border-radius: 3px;
        padding: 10px;
        box-shadow: 0px 0px 3px #999;

        .area {
            display: flex;
            align-items: center;
            padding: 10px;

            .area--title {
                width: 150px;
                text-align: right;
                padding-right: 20px;
                font-weight: bold;
                font-size: 14px;
            }
            .area--input {
                flex: 1;

                input {
                    width: 100%;
                    font-size: 14px;
                    padding: 5px;
                    border: 1px solid #ddd;
                    border-radius: 3px;
                    outline: 0;
                    transition: all ease 0.4s;

                    &:focus {
                        border: 1px solid #333;
                        color: #333;
                    }
                }
                button {
                    background-color: #3374db;
                    border: 0;
                    outline: 0;
                    padding: 5px 10px;
                    border-radius: 4px;
                    color: #fff;
                    font-size: 15px;
                    cursor: pointer;

                    &:hover {
                        color: #3374db;
                        background-color: #ffffff;
                        border: 1px solid #3374db;
                    }
                }
            }
        }
    }
    @media (max-width: 380px) {
        form {
            .area {
                .area--title {
                    width: 90px;
                    padding-right: 5px;
                    font-size: 12px;
                }
            }
        }
    }
`;
