import { LoginButton } from './LoginButton';
import { Profile } from './Profile';
import './nav.css';

export function Nav() {

    return (
        <>
            <nav>
                <ul>
                    
                    <li>
                        <a href="/users">Users</a>
                    </li>
                    <li>
                        <a href="/products">Products</a>
                    </li>
                    <li>
                        <a href="/sales">Sales</a>
                    </li>
                    <li>
                        <LoginButton />

                    </li>
                    <li>
                        <Profile />
                    </li>
                </ul>

            </nav>
        </>
    )
}

