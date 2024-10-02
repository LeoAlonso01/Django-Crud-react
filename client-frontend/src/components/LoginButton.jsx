import { useAuth0 } from '@auth0/auth0-react';
import React, { useState } from 'react';

export function LoginButton() {

    const { loginWithRedirect, isAuthenticated, logout } = useAuth0();

    return (
        <>
            {
                isAuthenticated ? <button className='btn-login' onClick={() => logout()} >Logout</button> :
                    <button className='btn-login' onClick={() => loginWithRedirect()} >Login</button>
            }
        </>

    )
}