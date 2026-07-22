from db_service import save_page

save_page(
    url="https://example.com",
    title="Test Page",
    content="Hello World",
    content_hash="123456"
)

print("Test record inserted!")