import React, { useState } from 'react';
import axiosInstance from '../../services/api';
import { useNavigate } from 'react-router-dom';

import PageContainer from '../../components/PageContainer';
import PageTitle from '../../components/PageTitle';
import { ErrorMessage } from '../../components/ErrorMessage';
import { PageArea } from './styled';

const Page = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [disabled, setDisabled] = useState(false);
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        setDisabled(true);
        setError('');

        axiosInstance
            .post(`token/`, {
                email: email,
                password: password,
            })
            .then((res) => {
                localStorage.setItem('access_token', res.data.access);
                localStorage.setItem('refresh_token', res.data.refresh);
                axiosInstance.defaults.headers['Authorization'] =
                    'JWT ' + localStorage.getItem('access_token');
                navigate('/');
            })
            .catch((err) => {
                setError(err);
                console.log(err);
            });
    };
    return (
        <PageContainer>
            <PageTitle>Login</PageTitle>
            <PageArea>
                {error && <ErrorMessage>{error}</ErrorMessage>}
                <form onSubmit={handleSubmit}>
                    <label className="area">
                        <div className="area--title">Email</div>
                        <div className="area--input">
                            <input
                                type="email"
                                disabled={disabled}
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>
                    </label>
                    <label className="area">
                        <div className="area--title">Senha</div>
                        <div className="area--input">
                            <input
                                type="password"
                                disabled={disabled}
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                    </label>
                    {/* <label className="area">
                        <div className="area--title">Lembrar Senha</div>
                        <div>
                            <input
                                type="checkbox"
                                disabled={disabled}
                                value={rememberPassword}
                                onChange={() =>
                                    setRememberPassword(!rememberPassword)
                                }
                            />
                        </div>
                    </label> */}
                    <label className="area">
                        <div className="area--title"></div>
                        <div className="area--input">
                            <button disabled={disabled}>Login</button>
                        </div>
                    </label>
                </form>
            </PageArea>
        </PageContainer>
    );
};

export default Page;
