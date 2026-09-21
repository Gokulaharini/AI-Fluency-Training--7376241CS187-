from config import client, MODEL


def main():
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: SETUP OK"
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()