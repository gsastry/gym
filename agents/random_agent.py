import gym

env = gym.make('OffSwitchCartpoleProb-v0')
env.reset()

for _ in range(100):
    obs = env.reset() # returns an initial observation
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        print("Observation: {}".format(obs))
        print("Action: {}".format(action))
        print("Reward: {}".format(reward))
        print("Info: {}".format(info))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

