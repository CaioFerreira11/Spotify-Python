# Spotify API Integration

This Python script interacts with the Spotify API to retrieve information about artists, their top tracks, and their albums. It uses the `requests` library to make API calls, `pandas` for data manipulation, and `dotenv` to securely manage API credentials.

## Features

- **Get Spotify Access Token**: Authenticates with the Spotify API using client credentials.
- **Search for Artist ID**: Retrieves the Spotify ID of an artist by their name.
- **Get Artist's Top Tracks**: Fetches the top tracks of a specified artist in a given market.
- **Get Artist's Albums**: Retrieves the albums of a specified artist, including release dates and years.
- **Convert Data to DataFrame**: Converts the retrieved data into a pandas DataFrame for easy analysis.

## Prerequisites

Before running the script, ensure you have the following:

1. **Spotify Developer Account**: Create an account on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and register an application to obtain your `CLIENT_ID` and `CLIENT_SECRET`.
2. **Python Libraries**: Install the required libraries using pip:
   ```bash
   pip install requests pandas python-dotenv

3. **Environment Variables**: Create a .env file in the root directory of your project and add your Spotify API credentials:
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret

1. Import the Required Libraries:

![image](https://github.com/user-attachments/assets/ed82bb2b-cccc-4e8a-bfe8-d0f7e443153f)

2. Load Environment Variables:
![image](https://github.com/user-attachments/assets/aba1e3a5-610d-4fd8-b13a-03b84c638906)

3. Set Pandas Display Options (optional):

![image](https://github.com/user-attachments/assets/179936d3-1773-43c5-8124-8a595bd63320)

4. Authenticate with Spotify API:

![image](https://github.com/user-attachments/assets/8c4c98df-2341-4fcc-ad00-1744df2b3a03)

5. Search for an Artist:

![image](https://github.com/user-attachments/assets/7b059136-c9f7-456d-997e-0241bd9f0857)

6. Get Artist's Top Tracks:

![image](https://github.com/user-attachments/assets/abaf2154-f258-41a0-824f-7e96803282cd)

7. Get Artist's Albums:

![image](https://github.com/user-attachments/assets/71a0f42f-9e39-4cb9-9d80-dbebd1d56c7e)

8. Convert Data to DataFrame:

![image](https://github.com/user-attachments/assets/b135ddca-a190-4fb7-b54c-db96243ee892)

9. Run the Script:

![image](https://github.com/user-attachments/assets/492b9baf-651f-4782-b68c-0d2b5640f63d)

## Example Output
The script will output a DataFrame containing the artist's albums, including the album name, artist name, release date, and year.

![image](https://github.com/user-attachments/assets/f3400f8a-0073-43fd-a590-5204dde673df)

