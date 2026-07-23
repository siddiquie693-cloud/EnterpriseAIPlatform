# -----------------------------
# Base Image
# -----------------------------
FROM python:3.12-slim

# -----------------------------
# Environment Variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Install System Dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Copy Requirements
# -----------------------------
COPY requirements.txt .

# -----------------------------
# Upgrade pip
# -----------------------------
RUN pip install --upgrade pip

# -----------------------------
# Install Python Dependencies
# -----------------------------
#RUN pip install \
   # --default-timeout=1000 \
    #--no-cache-dir \
    #--index-url https://download.pytorch.org/whl/cpu \
    #torch torchvision torchaudio

RUN pip install \
    --default-timeout=1000 \
    --retries=10 \
    --no-cache-dir \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements.txt    

# -----------------------------
# Copy Project Files
# -----------------------------
COPY . .
# Create logs directory
RUN mkdir -p logs

# -----------------------------
# Expose Django Port
# -----------------------------
EXPOSE 8000

# -----------------------------
# Start Django Development Server
# -----------------------------
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]