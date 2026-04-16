# rds_subnet = {
#   cidr              = ["10.0.8.0/24", "10.0.9.0/24"]
#   availability_zone = ["us-east-1a", "us-east-1b"]
# }

# rds_subnet = [
#   {
#     "name"              = "rds1"
#     "cidr"              = "10.0.8.0/24"
#     "availability_zone" = "us-east-1a"
#   },
#   {
#     "name"              = "rds2"
#     "cidr"              = "10.0.9.0/24"
#     "availability_zone" = "us-east-1b"
#   }

rds_subnet = [
  {
    name              = "rds1"
    cidr              = "10.0.8.0/24"
    availability_zone = "us-east-1a"
  },
  {
    name              = "rds2"
    cidr              = "10.0.9.0/24"
    availability_zone = "us-east-1b"
  }
]
