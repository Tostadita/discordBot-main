resource "aws_instance" "discord_instance"{

    ami = var.ami
    instance_type = var.instance_type

    tags = {
        Name = "${var.prefix}_discordBot_instance"
    }
    connection {
      type        = "ssh"
      host        = self.public_ip
      user        = "ubuntu"
      private_key = "discordbot-discord"
      timeout     = "4m"
   }
}