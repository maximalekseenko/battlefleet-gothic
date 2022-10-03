import socket
import _thread
import pickle
from backend.game import Game


class Server:
    def __init__(self) -> None:
        self.SERVER_ADDRESS = (socket.gethostbyname(socket.gethostname()), 5555)

        
        # start socket
        self.server_socket:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.SERVER_ADDRESS)
        self.server_socket.listen(2)

        # flags
        self.is_running = False

        # games
        self.games:list[Game] = list() 

        # log server init
        print("Server: initilized.")


    def Run(self):
        self.is_running = True

        # log server start
        print("Server: running.")

        # main loop
        while self.is_running:

            # get new connection
            new_client_socket, new_client_address = self.server_socket.accept()

            # log new connection
            print(f"{new_client_address}: connected.")

            # create new thread for connection
            _thread.start_new_thread(self.threaded_client, (new_client_socket, new_client_address))


    def threaded_client(self, client_socket, client_address):

        # try for dissconnections
        try:

            # attempt to get a game preferences form client
            game_prefs = pickle.loads(client_socket.recv(4096))

            # get game
            game = self.Get_Game(game_prefs)
            game.Connect(client_socket)

            # main loop
            while True:
                try:
                    client_socket.sendall(pickle.dumps(game.Get_Data()))
                    data = pickle.loads(client_socket.recv(4096))
                except: break
        except: pass

        # log loss of connection
        print(f"{client_address}: Lost connection")
        client_socket.close()


    def Get_Game(self, game_prefs) -> Game:
        
        # search for game
        for game in self.games:
            if game.Can_Join(game_prefs):
                return game
        
        # game not found
        # create new game
        new_game = Game(game_prefs)
        self.games.append(new_game)
        return new_game