import requests

base_url = "https://jsonplaceholder.typicode.com/"


def fetch_and_display_users(num_users):
    url = f"{base_url}users?_limit={num_users}"
    print(f"\n--- Requesting {num_users} users ---")
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            selected_users = data[:num_users]

            print(f"\n--- Displaying First {len(selected_users)} Users ---")

            for user in selected_users:
                try:
                    name = user["name"]
                    email = user["email"]
                    city = user["address"]["city"]
                    print(f"Name: {name} | Email: {email} | City: {city}")

                except (KeyError, TypeError) as data_err:
                    print(f"Warning: Skipped a user record. ({data_err})")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as net_err:
        print(f"Network Error: {net_err}")
        return None
    except ValueError:
        print("Error: Server response could not be parsed as JSON.")
        return None


fetch_and_display_users(4)
fetch_and_display_users(16)
