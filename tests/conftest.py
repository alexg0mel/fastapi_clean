import asyncio

import pytest
import pytest_asyncio


from app.documents.main import init_app as init_documents_app


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def documents():
    documents_app = init_documents_app()
    documents_app.test_url = "http://documents:5000"
    yield documents_app
