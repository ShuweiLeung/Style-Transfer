import matplotlib.pyplot as plt
from torch.autograd import Variable

def test_results_network(test_loader_A, test_loader_B, G_A, G_B, dataset):
    # test A to B
    n = 0
    for realA, _ in test_loader_A:
        n += 1
        path = dataset + '_results/test_results/AtoB/' + str(n) + '_input.png'
        plt.imsave(path, (realA[0].numpy().transpose(1, 2, 0) + 1) / 2)
        realA = Variable(realA.cuda(), volatile=True)
        genB = G_A(realA)
        path = dataset + '_results/test_results/AtoB/' + str(n) + '_output.png'
        plt.imsave(path, (genB[0].cpu().data.numpy().transpose(1, 2, 0) + 1) / 2)
        recA = G_B(genB)
        path = dataset + '_results/test_results/AtoB/' + str(n) + '_recon.png'
        plt.imsave(path, (recA[0].cpu().data.numpy().transpose(1, 2, 0) + 1) / 2)

    # test B to A
    n = 0
    for realB, _ in test_loader_B:
        n += 1
        path = dataset + '_results/test_results/BtoA/' + str(n) + '_input.png'
        plt.imsave(path, (realB[0].numpy().transpose(1, 2, 0) + 1) / 2)
        realB = Variable(realB.cuda(), volatile=True)
        genA = G_B(realB)
        path = dataset + '_results/test_results/BtoA/' + str(n) + '_output.png'
        plt.imsave(path, (genA[0].cpu().data.numpy().transpose(1, 2, 0) + 1) / 2)
        recB = G_A(genA)
        path = dataset + '_results/test_results/BtoA/' + str(n) + '_recon.png'
        plt.imsave(path, (recB[0].cpu().data.numpy().transpose(1, 2, 0) + 1) / 2)