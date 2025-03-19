import { createContext, useContext, useEffect, useState } from 'react';
import { IUser, IAuthCredentials } from '@/models/user';
import { authService } from '@/services/authService';

interface AuthContextType {
    user: IUser | null;
    isLoading: boolean;
    error: string | null;
    login: (credentials: IAuthCredentials) => Promise<void>;
    register: (credentials: IAuthCredentials) => Promise<void>;
    logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [user, setUser] = useState<IUser | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        checkAuth();
    }, []);

    async function checkAuth() {
        try {
            const isValid = await authService.verifyToken();
            if (isValid) {
                const user = await authService.getCurrentUser();
                setUser(user);
            }
        } catch (error) {
            setError('Authentication failed');
        } finally {
            setIsLoading(false);
        }
    }

    async function login(credentials: IAuthCredentials) {
        try {
            setIsLoading(true);
            setError(null);
            const user = await authService.login(credentials);
            setUser(user);
        } catch (error) {
            setError('Login failed');
            throw error;
        } finally {
            setIsLoading(false);
        }
    }

    async function register(credentials: IAuthCredentials) {
        try {
            setIsLoading(true);
            setError(null);
            const user = await authService.register(credentials);
            setUser(user);
        } catch (error) {
            setError('Registration failed');
            throw error;
        } finally {
            setIsLoading(false);
        }
    }

    async function logout() {
        try {
            setIsLoading(true);
            await authService.logout();
            setUser(null);
        } catch (error) {
            setError('Logout failed');
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <AuthContext.Provider value={{ user, isLoading, error, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}
