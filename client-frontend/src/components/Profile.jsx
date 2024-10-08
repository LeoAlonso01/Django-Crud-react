import React from 'react'
import { useAuth0 } from '@auth0/auth0-react';

export function Profile() {

    const { user, isAuthenticated } = useAuth0();

    return (
        
                isAuthenticated && (
                    <div className='profile-card' >
                        <img src={user.picture} alt={user.name} width={"50px"} height={"50px"} />
                        <h2>{user.name}</h2>
                        <p>{user.email}</p>
                    </div>
                ) 
                
            )
}
