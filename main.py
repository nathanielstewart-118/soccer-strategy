from get_player_data import PlayerRatingFetch


def main():

    playerRatingFetch = PlayerRatingFetch()
    # playerRatingFetch.fetch_player_data_from_fminside("Marc-Andre ter Stegen")

    # playerRatingFetch.fetch_player_data_from_ea("Marc-Andre ter Stegen")

    # playerRatingFetch.fetch_player_data_from_ea("Marc-Andre ter Stegen")

    playerRatingFetch.fetch_player_data_from_futbin("Marc-Andre ter Stegen")

main()