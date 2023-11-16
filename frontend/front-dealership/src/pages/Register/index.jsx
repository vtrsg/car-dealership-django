import React, { useState } from 'react';
import axiosInstance from '../../services/api';
import { useNavigate } from 'react-router-dom';

import PageContainer from '../../components/PageContainer';
import PageTitle from '../../components/PageTitle';
import { ErrorMessage } from '../../components/ErrorMessage';
import { PageArea } from './styled';
import { formatCPF } from '../../utils/formatCpf';

const Page = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [cpf, setCpf] = useState('');
    const [phone, setPhone] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [disabled, setDisabled] = useState(false);
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleChange = (e) => {
        const inputValue = e.target.value;
        const formattedCPF = formatCPF(inputValue);
        setCpf(formattedCPF);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setDisabled(true);
        setError('');

        if (password !== confirmPassword) {
            setError("the passwords don't match");
            setDisabled(false);
            return;
        }

        const firstName = name.split(' ')[0];
        const userName = name.split(' ').join('_');

        axiosInstance
            .post(`user/create/`, {
                email: email,
                user_name: userName,
                first_name: firstName,
                password: password,
                cpf: cpf,
                phone: phone,
            })
            .then((res) => {
                navigate('/signin');
                console.log(res);
                console.log(res.data);
            })
            .catch((err) => {
                setError(err.json());
                console.log(err);
            });
    };
    return (
        <PageContainer>
            <PageTitle>Cadastro</PageTitle>
            <PageArea>
                {error && <ErrorMessage>{error}</ErrorMessage>}
                <form onSubmit={handleSubmit}>
                    <label className="area">
                        <div className="area--title">Nome Completo</div>
                        <div className="area--input">
                            <input
                                type="text"
                                disabled={disabled}
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                required
                            />
                        </div>
                    </label>
                    <label className="area">
                        <div className="area--title">CPF</div>
                        <div className="area--input">
                            <input
                                type="text"
                                disabled={disabled}
                                value={cpf}
                                onChange={handleChange}
                                maxLength={14}
                                required
                            />
                        </div>
                    </label>
                    <label className="area">
                        <div className="area--title">Telefone</div>
                        <div className="area--input">
                            <input
                                type="text"
                                disabled={disabled}
                                value={phone}
                                onChange={(e) => setPhone(e.target.value)}
                                required
                            />
                        </div>
                    </label>
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
                    <label className="area">
                        <div className="area--title">Confirmar Senha</div>
                        <div className="area--input">
                            <input
                                type="password"
                                disabled={disabled}
                                value={confirmPassword}
                                onChange={(e) =>
                                    setConfirmPassword(e.target.value)
                                }
                                required
                            />
                        </div>
                    </label>

                    <label className="area">
                        <div className="area--title"></div>
                        <div className="area--input">
                            <button disabled={disabled}>Fazer Cadastro</button>
                        </div>
                    </label>
                </form>
            </PageArea>
        </PageContainer>
    );
};

export default Page;
