# 🚀 Oceanstar Travel - Vercel Deployment Guide

## 📋 Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Git Repository**: Push your code to GitHub/GitLab/Bitbucket
3. **Vercel CLI** (optional): `npm install -g vercel`

## 🗄️ Database Setup (Vercel Postgres - Free Tier)

### Step 1: Create Vercel Postgres Database
1. Go to your Vercel dashboard
2. Click "Storage" tab
3. Click "Create Database" 
4. Select "Postgres"
5. Choose "Hobby" (Free tier)
6. Name it: `oceanstar-travel-db`

### Step 2: Get Database Credentials
After creating the database, Vercel will provide these environment variables:
- `POSTGRES_URL`
- `POSTGRES_PRISMA_URL` 
- `POSTGRES_URL_NO_SSL`
- `POSTGRES_URL_NON_POOLING`
- `POSTGRES_USER`
- `POSTGRES_HOST`
- `POSTGRES_PASSWORD`
- `POSTGRES_DATABASE`

## 🌐 Deployment Steps

### Step 1: Deploy to Vercel
1. Push your code to GitHub
2. Connect GitHub repo to Vercel
3. Import project in Vercel dashboard
4. Vercel will auto-detect Django and use `vercel.json`

### Step 2: Configure Environment Variables
In Vercel dashboard → Project Settings → Environment Variables, add:

```
DEBUG=False
SECRET_KEY=your-super-secret-production-key-here
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

**Note**: Vercel will automatically set the POSTGRES_* variables when you create the database.

### Step 3: Initial Database Migration
After first deployment, run migrations:
1. Go to Vercel dashboard → Functions → View Function Logs
2. Or use Vercel CLI: `vercel env pull` then run locally with production DB

### Step 4: Create Production Superuser
You'll need to create a superuser for the production admin:
1. Connect to production database
2. Run: `python manage.py createsuperuser`

## 🔗 Your URLs After Deployment

- **Website**: `https://your-project-name.vercel.app`
- **Admin**: `https://your-project-name.vercel.app/en/admin/`

## ⚠️ Important Notes

### Vercel Postgres Free Tier Limits:
- **60 hours** compute time/month
- **512 MB** database storage
- **3 GB** data transfer/month

### Production vs Development:
- **Local**: Uses SQLite (`db.sqlite3`)
- **Production**: Uses PostgreSQL (Vercel Postgres)

### Data Migration:
Your current SQLite data will NOT automatically transfer to production.
You'll need to:
1. Export data from local SQLite
2. Import to production PostgreSQL
3. Or recreate content through admin panel

## 🛠️ Troubleshooting

### Build Fails?
- Check `requirements.txt` includes all dependencies
- Verify `vercel.json` configuration
- Check build logs in Vercel dashboard

### Database Connection Issues?
- Verify environment variables are set
- Check `DATABASE_URL` format
- Ensure database is running

### Static Files Not Loading?
- Run `python manage.py collectstatic` locally first
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Verify Vercel routes in `vercel.json`

## 🎉 You're Ready to Deploy!

Your Django app is now configured for Vercel Postgres deployment!