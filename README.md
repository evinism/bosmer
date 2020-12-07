# Bosmer: Boring S3 migration tool

### Proposed CLI

```
# Create a bosmer repository titled `[s3_bucket]` the current directory, and marks
# Marks an S3 bucket for use with a certain bosmer repository
bosmer init [s3_bucket]

# Generates a migration
bosmer generate [migration_name]

# Apply all pending migrations to an s3 bucket.
bosmer migrate

# Roll down the most recently run migration
bosmer rollback

```
