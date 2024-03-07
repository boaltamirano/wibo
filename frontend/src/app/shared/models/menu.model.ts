export interface Menu {
    id: string;
    name: string;
    price: number;
    description: string;
    image: string;
    rating: number;
    total: number;
    amount: number;
}

export interface CustomResponse {
    ok:      boolean,
    message: string,
    body:    [],
    status:  number
}