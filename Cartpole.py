import gym
env = gym.make('Acrobot-v1')
for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        #action = env.action_space.sample() # comentario
        action = 1
        observation, reward, done, info = env.step(action)
        print (env.action_space)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
