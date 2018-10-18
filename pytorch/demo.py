import torch
import torchvision.utils as vutils
import torchvision.transforms as transforms
import os, argparse
from PIL import Image
import models.silnet as silnet


def demo(config):
    input = Image.open(config.img_path).convert('RGB')
    input = transforms.ToTensor()(input)
    input = input.unsqueeze(0)

    SilNet = silnet.UNet(3, 1)
    SilNet.load_state_dict(torch.load('Pretrained_SilNet.pth', map_location='cpu'))

    output = SilNet(input)
    vutils.save_image(output.data, '%s/output.png' % config.outf, nrow=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', required=True, type=str, help='path to your demo image')
    parser.add_argument('--outf', required=True, help='output folder.')
    config = parser.parse_args()

    if not os.path.exists(config.outf):
        os.makedirs(config.outf)

    demo(config)