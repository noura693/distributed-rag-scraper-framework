from db_service import save_page

save_page(
    url="https://example.com",
    title="Page",
    content="Version 1",
    content_hash="abc"
)

save_page(
    url="https://example.com",
    title="Page",
    content="Version 1",
    content_hash="abc"
)

save_page(
    url="https://example.com",
    title="Page",
    content="Version 2",
    content_hash="xyz"
)