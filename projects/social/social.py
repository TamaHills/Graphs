import random

class Queue():
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        count = 0
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        # Shuffle the list
        random.shuffle(possible_friendships)
        # Grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            count += 1
            self.add_friendship(friendship[0], friendship[1])
        print(count)

    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = num_users
        self.users = {i+1:f'User {i+1}' for i in range(num_users)}
        self.friendships = {i+1:set() for i in range(num_users)}
        n_friendships = 0
        while n_friendships < num_users * avg_friendships:
            friend_1, friend_2 = random.randint(1,num_users), random.randint(1,num_users)
            if self.add_friendship(friend_1, friend_2):
                n_friendships += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        q.enqueue([user_id])
        visited = {user_id:[user_id]}  # Note that this is a dictionary, not a set
        while len(q) > 0:
            path = q.dequeue()
            u = path[-1]
            for friend in self.friendships[u]:
                if friend not in visited:
                    visited[friend] = path

                    q.enqueue(path + [friend])

        return visited


if __name__ == '__main__':
    n = 1000
    avg = 5
    sg = SocialGraph()
    sg.populate_graph(n, avg)
    print(sg.friendships)
    connections = sg.get_all_social_paths(random.randint(1, n))
    print(connections)
    print( (len(connections.keys()) * 100) // n)
    avg_len = 0
    for key in connections.keys():
        avg_len += len(connections[key])
    
    avg_len /= len(connections.keys())
    print(avg_len)

