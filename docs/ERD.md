# Entity-Relationship Diagram

```mermaid
erDiagram
    CATEGORIES ||--o{ PRODUCTS : contains
    CATEGORIES {
        int category_id PK
        varchar category_name
    }
    PRODUCTS {
        int product_id PK
        varchar name
        int category_id FK
        decimal price
        int stock_quantity
        timestamp last_updated
    }
```
