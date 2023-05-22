from model import Model

# Initialize the model with your chosen parameters
model = Model(width=10, height=10, num_fish=100, num_fisheries=10, num_ports=5)

num_steps = 100

for i in range(num_steps):
    model.step()

print(len(model.fish))