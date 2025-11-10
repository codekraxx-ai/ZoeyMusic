def git():
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    # If DISABLE_UPDATE is set, skip git operations
    if os.getenv("DISABLE_UPDATE", "False") == "True":
        LOGGER(__name__).info("Auto-update disabled via DISABLE_UPDATE variable.")
        return

    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
        origin = repo.remotes.origin
        origin.fetch()
        LOGGER(__name__).info("Fetching updates from upstream repository...")
    except InvalidGitRepositoryError:
        LOGGER(__name__).warning("No .git repo found, skipping auto-update.")
    except GitCommandError as e:
        LOGGER(__name__).warning(f"Git command failed, skipping auto-update. Details: {e}")
    except Exception as e:
        LOGGER(__name__).warning(f"Unexpected error in git updater: {e}")
