import sys

import gym
from gym import wrappers


class RandomAgent(object):
    """I do random stuff."""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, obs, reward, done):
        return self.action_space.sample()

if __name__ == '__main__':
    env = gym.make('DoubleDunk-v0')
    agent = RandomAgent(env.action_space)

    num_episodes = 100
    reward = 0
    done = False

    for _ in range(num_episodes):
        obs = env.reset() # returns an initial observation
        while True:
            env.render()
            action = agent.act(obs, reward, done)
            obs, reward, done, info = env.step(action)
            print("Observation: {}".format(obs))
            print("Action: {}".format(action))
            print("Reward: {}".format(reward))
            print("Info: {}".format(info))
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break

