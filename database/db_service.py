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
from sqlalchemy.orm import sessionmaker
from db import engine
from models import Page, PageVersion

SessionLocal = sessionmaker(bind=engine)


def save_page(url, title, content, content_hash):

    session = SessionLocal()

    existing_page = (
        session.query(Page)
        .filter(Page.url == url)
        .first()
    )

    # New page
    if not existing_page:

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

        print("New page added")

        return

    # Same content -> skip
    if existing_page.content_hash == content_hash:

        print("Duplicate page skipped")

        session.close()

        return

    # Content changed -> new version
    latest_version = (
        session.query(PageVersion)
        .filter(
            PageVersion.page_id ==
            existing_page.id
        )
        .count()
    )

    version = PageVersion(
        page_id=existing_page.id,
        content=content,
        version=latest_version + 1
    )

    existing_page.content_hash = content_hash

    session.add(version)
    session.commit()

    session.close()

    print("New page version created")
