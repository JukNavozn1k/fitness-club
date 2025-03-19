import { IAuthCredentials, IAuthToken, IUser } from '@/models/user';
import { $api } from '@/core/api/axios';

export interface IAuthRepository {
    login(credentials: IAuthCredentials): Promise<IAuthToken>;
    register(credentials: IAuthCredentials): Promise<IUser>;
    logout(): Promise<void>;
    getCurrentUser(): Promise<IUser>;
    verifyToken(token: string): Promise<boolean>;
}

export class AuthRepository implements IAuthRepository {
    async login(credentials: IAuthCredentials): Promise<IAuthToken> {
        const response = await $api.post<IAuthToken>('/auth/login', credentials);
        return response.data;
    }

    async register(credentials: IAuthCredentials): Promise<IUser> {
        const response = await $api.post<IUser>('/auth/register', credentials);
        return response.data;
    }

    async logout(): Promise<void> {
        localStorage.removeItem('token');
    }

    async getCurrentUser(): Promise<IUser> {
        const response = await $api.get<IUser>('/auth/me');
        return response.data;
    }

    async verifyToken(token: string): Promise<boolean> {
        const response = await $api.get<{ valid: boolean }>('/auth/verify-token');
        return response.data.valid;
    }
}

export const authRepository = new AuthRepository();
