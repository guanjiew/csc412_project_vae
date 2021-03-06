import argparse

from helper import str2bool

parser = argparse.ArgumentParser(description='Beta-VAE Model')

# Task specify
parser.add_argument('--dataset', default='pathmnist', type=str, help='dataset name', choices=['pathmnist'])
parser.add_argument('--train', default=True, type=str2bool, help='train or test')
parser.add_argument('--is_classification', default=False, type=bool, help='whether we are doing classification')

# Model architecture
parser.add_argument('--is_PID', default=True, type=str2bool, help='if use pid or not')
parser.add_argument('--beta', default=4, type=float, help='beta parameter for KL-term in original beta-VAE')
parser.add_argument('--beta1', default=0.9, type=float, help='Adam optimizer beta1')
parser.add_argument('--beta2', default=0.999, type=float, help='Adam optimizer beta2')
parser.add_argument('--vae_model', default='betavaeh', type=str,
                    help='vae_model proposed in Higgins et al. or Burgess et al. H/B')

# Hyper parameters
parser.add_argument('--max_iter', default=900, type=float, help='maximum training iteration')
parser.add_argument('--batch_size', default=16, type=int, help='batch size')
parser.add_argument('--limit', default=3, type=float, help='traverse limits')
parser.add_argument('--KL_loss', default=200, type=float, help='KL KL_divergence')
parser.add_argument('--pid_fixed', default=False, type=str2bool, help='if fixed PID or dynamic')
parser.add_argument('--z_dim', default=500, type=int, help='dimension of the representation z')
parser.add_argument('--gamma', default=1000, type=float, help='gamma parameter for KL-term in understanding '
                                                              'beta-VAE')
parser.add_argument('--C_max', default=25, type=float, help='capacity parameter(C) of bottleneck channel')
parser.add_argument('--C_stop_iter', default=5e5, type=float, help='when to stop increasing the capacity')
parser.add_argument('--lr', default=1e-4, type=float, help='learning rate')

# Specify environment settings
parser.add_argument('--seed', default=1, type=int, help='random seed')
parser.add_argument('--cuda', default=True, type=str2bool, help='enable cuda')
parser.add_argument('--image_size', default=128, type=int, help='image size. now only (64,64) is supported')
parser.add_argument('--num_workers', default=2, type=int, help='dataloader num_workers')

# Path
parser.add_argument('--dset_dir', default='data', type=str, help='dataset directory')
parser.add_argument('--save_output', default=True, type=str2bool, help='save traverse images and gif')
parser.add_argument('--output_dir', default='outputs', type=str, help='output directory')
parser.add_argument('--ckpt_dir', default='checkpoints', type=str, help='checkpoint directory')
parser.add_argument('--ckpt_name', default='last', type=str,
                    help='load previous checkpoint. insert checkpoint filename')

# Visualization
parser.add_argument('--viz_on', default=False, type=str2bool, help='enable visdom visualization')
parser.add_argument('--viz_name', default='main', type=str, help='visdom env name')
parser.add_argument('--viz_port', default=8097, type=str, help='visdom port number')
parser.add_argument('--gather_step', default=9, type=int,
                    help='numer of iterations after which data is gathered for visdom')
parser.add_argument('--display_step', default=9, type=int,
                    help='number of iterations after which loss data is printed and visdom is updated')
parser.add_argument('--save_step', default=450, type=int,
                    help='number of iterations after which a checkpoint is saved')
parser.add_argument('--delta', default=0.01, type=float, help='delta used for epsilon delta posterior collapse visualization')
parser.add_argument('--aggressive', default=False, type=bool, help='whether the encoder is trained more aggressively than the decoder')
parser.add_argument('--agg_iter', default=5, type=int, help='number of times to train the encoder aggressively')
