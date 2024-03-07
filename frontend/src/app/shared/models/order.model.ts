export interface Order {
    id:       string
    table:    number;
    menus:    Menu[];
    subtotal: 0;
    total:    0;
    tip:      0;
    state:    boolean;
    user:     string;
}

interface Menu {
    nemu:     string;
    amount:   number;
    subtotal: number;
}