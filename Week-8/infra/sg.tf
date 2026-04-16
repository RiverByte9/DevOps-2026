# # 3 security groups

# # ALB SG
# resource "aws_security_group" "alb" {
#   name        = "${var.prefix}-${var.app_name}-alb-sg"
#   description = "security group for ALB"
#   #vpc_id      = aws_vpc.main.id 
#   vpc_id = module.network.vpc_id


#   # ingress {
#   #     from_port   = 80
#   #     to_port     = 80
#   #     protocol    = "tcp"
#   #     cidr_blocks = ["0.0.0.0/0"]
#   # }

#   # ingress {
#   #     from_port   = 443
#   #     to_port     = 443
#   #     protocol    = "tcp"
#   #     cidr_blocks = ["0.0.0.0/0"]
#   # }

#   dynamic "ingress" {
#     for_each = toset(var.alb_port_list)
#     content {
#       from_port   = ingress.value.from_port
#       to_port     = ingress.value.to_port
#       protocol    = "tcp"
#       cidr_blocks = ["0.0.0.0/0"]

#     }
#   }


#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# # ECS SG
# resource "aws_security_group" "ecs" {
#   for_each = local.ecs_services_map
#   name        = "${var.prefix}-${var.app_name}-${each.key}-sg"
#   description = "security group for ECS tasks"
#   vpc_id      = module.network.vpc_id

#   # ingress {
#   #   from_port       = var.container_port
#   #   to_port         = var.container_port
#   #   protocol        = "tcp"
#   #   security_groups = [aws_security_group.alb.id]
#   # }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# resource "aws_security_group_rule" "frontend_ingress" {
#   type = "ingress"
#   from_port = 80
#   to_port = 80
#   protocol = "tcp"
#   security_group_id = aws_security_group.ecs["frontend"].id
#   source_security_group_id = aws_security_group.alb.id
#   depends_on = [aws_security_group.ecs]
# }
# resource "aws_security_group_rule" "backend_ingress" {
#   type = "ingress"
#   from_port = 8000
#   to_port = 8000
#   protocol = "tcp"
#   security_group_id = aws_security_group.ecs["backend"].id
#   source_security_group_id = aws_security_group.ecs["frontend"].id
#   depends_on = [aws_security_group.ecs]


# }



# # RDS SG
# resource "aws_security_group" "rds" {
#   name        = "${var.prefix}-${var.app_name}-rds-sg"
#   description = "security group for RDS instance"
#   vpc_id      = module.network.vpc_id

#   # ingress {
#   #   from_port       = 5432
#   #   to_port         = 5432
#   #   protocol        = "tcp"
#   #   security_groups = [aws_security_group.ecs["backend"].id]

#   # }
#   # Add this new separate rule instead:
# resource "aws_security_group_rule" "rds_from_backend" {
#   type                     = "ingress"
#   from_port                = 5432
#   to_port                  = 5432
#   protocol                 = "tcp"
#   security_group_id        = aws_security_group.rds.id
#   source_security_group_id = aws_security_group.ecs["backend"].id
#   depends_on               = [aws_security_group.ecs, aws_security_group.rds]
# }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }


#----new on==========

# 3 security groups

# ALB SG
resource "aws_security_group" "alb" {
  name        = "${var.prefix}-${var.app_name}-alb-sg"
  description = "security group for ALB"
  vpc_id      = module.network.vpc_id

  dynamic "ingress" {
    for_each = toset(var.alb_port_list)
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ECS SG
resource "aws_security_group" "ecs" {
  for_each    = local.ecs_services_map
  name        = "${var.prefix}-${var.app_name}-${each.key}-sg"
  description = "security group for ECS tasks"
  vpc_id      = module.network.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "frontend_ingress" {
  type                     = "ingress"
  from_port                = 80
  to_port                  = 80
  protocol                 = "tcp"
  security_group_id        = aws_security_group.ecs["frontend"].id
  source_security_group_id = aws_security_group.alb.id
  depends_on               = [aws_security_group.ecs]
}

resource "aws_security_group_rule" "backend_ingress" {
  type                     = "ingress"
  from_port                = 8000
  to_port                  = 8000
  protocol                 = "tcp"
  security_group_id        = aws_security_group.ecs["backend"].id
  source_security_group_id = aws_security_group.ecs["frontend"].id
  depends_on               = [aws_security_group.ecs]
}

# RDS SG
resource "aws_security_group" "rds" {
  name        = "${var.prefix}-${var.app_name}-rds-sg"
  description = "security group for RDS instance"
  vpc_id      = module.network.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# This is OUTSIDE the aws_security_group.rds block
resource "aws_security_group_rule" "rds_from_backend" {
  type                     = "ingress"
  from_port                = 5432
  to_port                  = 5432
  protocol                 = "tcp"
  security_group_id        = aws_security_group.rds.id
  source_security_group_id = aws_security_group.ecs["backend"].id
  depends_on               = [aws_security_group.ecs, aws_security_group.rds]
}