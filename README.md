### Arch Diagram

tts
- shadeform cloud gpu instance 1
    - kokoro (service 1)
        - `kokoro_api.py` - **Flask Entrypoint**
        - `kokoro flask flas_cors numpy torch librosa (audio processing)
    - neurosync (service 2) - convert tts audio "feelings" to microexpressions
        - `NeuroSync_Local_API/neurosync_local_api` - **Flask Entrypoint**
    - whispher
    - unreal engine
    - React Frontend
        - WebRTC Server - Audio/Video
    - Apache Kafka
    