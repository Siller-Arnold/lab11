{{- define "users-api.name" -}}
users-api
{{- end }}

{{- define "users-api.fullname" -}}
users-api
{{- end }}

{{- define "users-api.serviceAccountName" -}}
{{- if .Values.serviceAccount.name }}
{{ .Values.serviceAccount.name }}
{{- else }}
{{ include "users-api.fullname" . }}
{{- end }}
{{- end }}
