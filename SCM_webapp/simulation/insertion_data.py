from decimal import Decimal

orders_data = [
    {
        "order_id": 1001,
        "customer_id": 1,
        "total_amount": Decimal('500.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5001,
                "tracking_number": "TRK001",
                "status": "Pending",
                "items": [
                    {"inventory_id": 1, "quantity": 2, "amount": Decimal('200.00')},
                    {"inventory_id": 2, "quantity": 1, "amount": Decimal('100.00')}
                ]
            },
            {
                "shipping_id": 5002,
                "tracking_number": "TRK002",
                "status": "Pending",
                "items": [
                    {"inventory_id": 3, "quantity": 2, "amount": Decimal('200.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1002,
        "customer_id": 2,
        "total_amount": Decimal('350.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5003,
                "tracking_number": "TRK003",
                "status": "Pending",
                "items": [
                    {"inventory_id": 4, "quantity": 3, "amount": Decimal('150.00')}
                ]
            },
            {
                "shipping_id": 5004,
                "tracking_number": "TRK004",
                "status": "Pending",
                "items": [
                    {"inventory_id": 5, "quantity": 2, "amount": Decimal('200.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1003,
        "customer_id": 3,
        "total_amount": Decimal('220.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5005,
                "tracking_number": "TRK005",
                "status": "Pending",
                "items": [
                    {"inventory_id": 6, "quantity": 1, "amount": Decimal('120.00')},
                    {"inventory_id": 1, "quantity": 2, "amount": Decimal('100.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1004,
        "customer_id": 4,
        "total_amount": Decimal('300.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5006,
                "tracking_number": "TRK006",
                "status": "Pending",
                "items": [
                    {"inventory_id": 2, "quantity": 3, "amount": Decimal('300.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1005,
        "customer_id": 5,
        "total_amount": Decimal('420.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5007,
                "tracking_number": "TRK007",
                "status": "Pending",
                "items": [
                    {"inventory_id": 3, "quantity": 2, "amount": Decimal('180.00')},
                    {"inventory_id": 4, "quantity": 1, "amount": Decimal('240.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1006,
        "customer_id": 1,
        "total_amount": Decimal('270.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5008,
                "tracking_number": "TRK008",
                "status": "Pending",
                "items": [
                    {"inventory_id": 5, "quantity": 3, "amount": Decimal('270.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1007,
        "customer_id": 2,
        "total_amount": Decimal('190.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5009,
                "tracking_number": "TRK009",
                "status": "Pending",
                "items": [
                    {"inventory_id": 6, "quantity": 1, "amount": Decimal('190.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1008,
        "customer_id": 3,
        "total_amount": Decimal('320.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5010,
                "tracking_number": "TRK010",
                "status": "Pending",
                "items": [
                    {"inventory_id": 1, "quantity": 4, "amount": Decimal('320.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1009,
        "customer_id": 4,
        "total_amount": Decimal('610.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5011,
                "tracking_number": "TRK011",
                "status": "Pending",
                "items": [
                    {"inventory_id": 2, "quantity": 5, "amount": Decimal('500.00')}
                ]
            },
            {
                "shipping_id": 5012,
                "tracking_number": "TRK012",
                "status": "Pending",
                "items": [
                    {"inventory_id": 3, "quantity": 2, "amount": Decimal('110.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1010,
        "customer_id": 5,
        "total_amount": Decimal('260.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5013,
                "tracking_number": "TRK013",
                "status": "Pending",
                "items": [
                    {"inventory_id": 4, "quantity": 2, "amount": Decimal('160.00')},
                    {"inventory_id": 5, "quantity": 1, "amount": Decimal('100.00')}
                ]
            }
        ]
    }
]
