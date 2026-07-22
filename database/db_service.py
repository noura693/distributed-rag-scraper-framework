from sqlalchemy.orm import sessionmaker
from db import engine
from models import Page, PageVersion

SessionLocal = sessionmaker(bind=engine)


def save_page(url, title, content, content_hash):

    session = SessionLocal()

    page = Page(
        url=url,
        title=title,
        content_hash=content_hash
    )

    session.add(page)
    session.commit()
    session.refresh(page)

    version = PageVersion(
        page_id=page.id,
        content=content,
        version=1
    )

    session.add(version)
    session.commit()

    session.close()