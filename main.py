
import httpx
from pydantic import BaseModel, ValidationError


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()

        post = Post.model_validate(response.json())

        print("Post ID:", post.id)
        print("Title:", post.title)
        print("Body:", post.body)

    except httpx.HTTPError as error:
        print("API request failed:", error)
    except ValidationError as error:
        print("Invalid API response:", error)


if __name__ == "__main__":
    main()
