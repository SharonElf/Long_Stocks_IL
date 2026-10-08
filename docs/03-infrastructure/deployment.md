# Deployment

## Where it runs

- **Production:** _e.g., AWS us-east-1, ECS Fargate_
- **Staging:** _e.g., same as prod, smaller instances_
- **Local dev:** _e.g., Docker Compose, see `docs/00-quickstart.md`_

## How it ships

- Trigger: _e.g., merge to `main` → auto-deploy to staging; tag `v*` → deploy to prod_
- Pipeline: _e.g., GitHub Actions workflow `.github/workflows/deploy.yml`_
- Build artifact: _e.g., Docker image, pushed to ECR with commit SHA tag_
- Approval gates: _e.g., prod requires manual approval from any teammate_

## Rollback

Documented in `runbooks/rollback.md`. Should take < 5 minutes.

## Environments

| Env | URL | Branch | Auto-deploy? |
|-----|-----|--------|--------------|
| Production | _https://..._ | `v*` tags | No (manual approval) |
| Staging | _https://staging..._ | `main` | Yes |
| Preview | _per-PR_ | _per-PR_ | Yes |

## Infrastructure as code

- Tool: _e.g., Terraform, Pulumi, CDK_
- Location: _e.g., `infra/` folder_
- Apply process: _via CI on merge; never `terraform apply` from a laptop_
